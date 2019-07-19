%Read the image from the local disk
fileId=fopen('E:\ASU\Courses\1st Sem\Computer Systems - I\lena.raw','r');
data=fread(fileId);                                                        %read the data from the image
data=reshape(data,[512 512]);   
data=data';
%Read the original data for DCT
 
orig_img=data;
imshow(orig_img);

% Define block size for segementation
 
blocksize=8;

% Calculate the DCT transform matrix DCT_Trans
i = 0;
for j = 0: blocksize - 1
  DCT_trans(i + 1, j + 1) = sqrt(1 / blocksize) ...
                          * cos ((2 * j + 1) * i * pi / (2 * blocksize));
end
 
for i = 1: blocksize - 1
  for j = 0: blocksize - 1
    DCT_trans(i + 1, j + 1) = sqrt(2 / blocksize) ...
                            * cos ((2 * j + 1) * i * pi / (2 * blocksize));
  end
end

sz = size(orig_img);
rows = sz(1,1);               % finds image's rows and columns
cols = sz(1,2);


% Because the DCT is designed to work on pixel values ranging from -128 to 127, the original
%block is ?leveled off?
%by subtracting 128 from each entry. 

orig_img=orig_img-128;

DCT_quantizer = ...    % levels for quantizing the DCT block (8x8 matrix)
    [ 16  11  10  16  24  40  51  61; ...
      12  12  14  19  26  58  60  55; ...
      14  13  16  24  40  57  69  56; ...
      14  17  22  29  51  87  80  62; ...
      18  22  37  56  68 109 103  77; ...
      24  35  55  64  81 104 113  92; ...
      49  64  78  87 103 121 120 101; ...
      72  92  95  98 112 100 103  99 ];

 
quant_multiple = 0.05;    % set the multiplier to change size of quant. levels
                       % (The values of this defines the number of zero
                       % coefficients)
  
% Take DCT of blocks of size blocksize
 fprintf(1, '\nFinding the DCT and quantizing...\n');
starttime = cputime;              % "cputime" is an internal cpu time counter
 
jpeg_img = orig_img - orig_img;   % zero the matrix for the compressed image

for row = 1: blocksize: rows
  for col = 1: blocksize: cols
       % take a block of the image:
    DCT_matrix = orig_img(row: row + blocksize-1, col: col + blocksize-1);
       % perform the transform operation on the 2-D block
     DCT_matrix = DCT_trans * DCT_matrix * DCT_trans';
      % quantize it (levels stored in DCT_quantizer matrix):
      DCT_matrix = floor (DCT_matrix ...
          ./ (DCT_quantizer(1:blocksize, 1:blocksize) * quant_multiple)+0.5);
      % place it into the compressed-image matrix:
    jpeg_img(row: row + blocksize-1, col: col + blocksize-1) = DCT_matrix;
 
  end
end

% Reverse the process (take the Inverse DCT)
 
fprintf(1, 'Reconstructing quantized values and taking the inverse DCT...\n');
starttime = cputime;
 
recon_img = orig_img - orig_img;  % zero the matrix for the reconstructed image
 
for row = 1: blocksize: rows
  for col = 1: blocksize: cols
 
       % take a block of the image:
    IDCT_matrix = jpeg_img(row: row + blocksize-1, col: col + blocksize-1);
 
       % reconstruct the quantized values:
    IDCT_matrix = IDCT_matrix ...
                .* (DCT_quantizer(1:blocksize, 1:blocksize) * quant_multiple);
 
       % perform the inverse DCT:
    IDCT_matrix = DCT_trans' * IDCT_matrix * DCT_trans;
 
       % place it into the reconstructed image:
    recon_img(row: row + blocksize-1, col: col + blocksize-1) = IDCT_matrix;
 
  end
end

%Adding 128 as we substracted 128 from the original image
 
orig_img=orig_img+128;
recon_img=recon_img+128;

% Calculate signal-to-noise ratio
 
fprintf(1, 'Finding the signal-to-noise ratio...\n');
 
 
PSNR = 0;
for row = 1:rows
  for col = 1:cols
    PSNR = PSNR + (orig_img(row, col) - recon_img(row, col)) ^ 2;
  end
end
PSNR = 10 * log10 ((255^2) / (1 / (((rows + cols) / 2) ^ 2) * PSNR));
             % (averaged rows and cols together)


% Plot the original, compressed and deconstructed image.
figure(1)
subplot(3,2,1), image(data), title('Original Image');
subplot(3,2,2), image(jpeg_img), title('compressed Image with one half the coefficients in each blocks to be zero');
subplot(3,2,3), image(recon_img), title('reconstructed Image where one half the coefficient in each block is zero');
 
             
fprintf(1, '\nThe signal-to-noise ratio (PSNR) for one half of the coefficient to be zero is: %1.3f dB\n\n', PSNR);

% Code the image
 
% No of non zero elements in the matrix
n=0;
n=nnz(jpeg_img);
%Total bits to code the image
tb=0;
tb=n*10;
%Average no of bits per pixel
Avg_bits=0;
Avg_bits=tb/(512*512);  
fprintf(1, '\nThe total no of bits used to code the image is:%1.3f\n', tb); %#ok<CTPCT>
fprintf(1, '\nThe average no of bits per pixel is: %1.3f\n', Avg_bits); %#ok<CTPCT>


%Plot 2D DFT magnitude spectrum of original signal
fs = 1000;
t = 0:1/fs:1-(1/fs);
X1 = fftshift(fft(data));
X1 = abs(X1);
subplot(3,2,4)
plot(X1/fs);
title('Magnitude Spectrum of original signal');
 
X2=fftshift(fft(recon_img));
X2=abs(X2);
subplot(3,2,5)
plot(X1/fs);
title('Magnitude Spectrum of reconstructed image signal');
