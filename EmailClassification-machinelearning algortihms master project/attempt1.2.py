"""
This script can be used as skelton code to read the challenge train and test
csvs, to train a trivial model, and write data to the submission file.
"""
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer

ID_FIELD, DATE_FIELD, ORG_FIELD, TLD_FIELD, CCS_FIELD, BCCED_FIELD, MAIL_TYPE_FIELD, IMAGES_FIELD, URLS_FIELD, SALUTATIONS_FIELD, DESIGNATION_FIELD, CHARS_IN_SUBJECT_FIELD, CHARS_IN_BODY_FIELD, LABEL_FIELD = 'Id', 'date', 'org', 'tld', 'ccs', 'bcced', 'mail_type', 'images', 'urls', 'salutations', 'designation', 'chars_in_subject', 'chars_in_body', 'label'

ALL_FIELDS = [ ORG_FIELD, TLD_FIELD, CCS_FIELD, BCCED_FIELD, MAIL_TYPE_FIELD, IMAGES_FIELD, URLS_FIELD, SALUTATIONS_FIELD, DESIGNATION_FIELD, CHARS_IN_SUBJECT_FIELD, CHARS_IN_BODY_FIELD, LABEL_FIELD ]

ORG_CATEGORIES = [ 'gmail', 'news', 'iiitd', 'statebankrewardz', 'shop', 'quora', 'linkedin', 'topcoder', 'amazon', 'crazydomains', 'medium', 'centralesupelec', 'autodesk', 'redwolf', 'naaptoldeals', 'usebackpack', 'mapbox', 'awseducate', 'mailer', 'udacity', 'marketing', 'flipkartletters', 'pvrcinemas', 'em', 'youtube', 'crm', 'twitter', 'paytmemail', 'github', 'reply', 'mail', 'applemusic', 'mails', 'codeschool', 'khanacademy', 'web-spicejet', 'hackerearth', 'e', 'notifications', 'coupondunia', 'bigbasket', 'innerchef', 'emm', 'angel', 'sampark', 'emailer', 'entertainment', 'newsletter', 'mentor', 'airtable', 'updates', 'kaggle', 'htc', 'docker', 'explore', 'm', 'magoosh', 'arya', 'asuswebstorage', 'pinterest', 'truecaller', 'rcgroups', 'researchgatemail', 'edx', 'inria', 'researchgate', 'indiatimes', 'plus', 'nvidia', 'iheartdogs-email', 'newsgram', 'facebookmail', 'bookmyshow', 'rs-components', 'maillist', 'neo4j', 'imdb', 'phonepe', 'payumoney', 'e-mail', 'primevideo', 'overleaf', 'interviewbit', 'dataquest-0740d8e6e13d', 'ieee', 'cdconnect', 'go', 'mak', 'edm', 'ecp', 'xprize', 'donate', 'thomascook', 'unisys', 'oneplus', 'ndtvecommerce', 'academia-mail', 'careers360', 'discuss', 'flipkartmail', 'signalprocessingsociety', 'send', 'nedm', 'email', 'box8letters', 'duolingo', 'twenty19', 'youth4work', 'magento', 'referhire', 'datacamp', 'healthie', 'inoxmovies', 'myopportunity', 'springboard', 'rapidapi', 'airpostmail', 'usief', 'airvistara', 'symless', 'ride', 'hackerrank', 'trello', 'paypal-exchanges', 'deeplearning', 'critical', 'technolutions', 'creately', 'codecademy', 'flipkartpromotions', 'walkfree', 'digitalglobe-platform', 'googlegroups', 'invite', 'glassdoor', 'cambridge-intelligence', 'pbmail', 'monsterindia', 'cs', 'new', 'getpostman', 'naaptoldealz', 'airtable-2', 'simbla', 'codeanywhere', 'oracle-mail', 'messages', 'bg', 'stackexchange', 'brilliant', 'dropbox', 'tufinawatches', 'travel', 'uber', 'emails', 'outernet', 'vairdo', 'agencenavigo', 'supelec', 'cleartrip', 'repositoryhosting', 'geeps', 'sg', 'witai-2', 'clubvistara', 'nptel', 'mp1', 'neotechnology', 'diydrones', 'blablacar', 'cbsnewsletter', 'ruprr', 'Neotechnology', 'Magento', 'foursquare', 'flat', 'kotak', 'google', 'stylusstudio', 'rcbazaar', 'freshworks', 'internations', 'astrospeak', 'student-cs', 'ZOONIVERSE', 'policies', 'cromaretail', 'sutlej-mail', 'marmalademail', 'dropboxmail', 'shining3d', 'ni', 'pornhub', 'media', 'in', 'sci', 'centrepompidou', 'sc', 'tatadocomo', 'makemytripmails', 'comma', 'sbi', 'flipkart', 'smartsheet', 'info', 'oneplusstore', 'insure', 'zoomgroup', 'quadkopters', 'premiumjobalerts', 'dcoder', 'mail1', 'lss', 'diux', 'connect', 'ampleclick', 'fccashback', '3dr', 'asvspoof', 'entropay', 'communication', 'vito', 'cardekholetters', 'promo', 'blablacar', 'cdconnect', 'pbmail', 'insure', 'makemytripmails', 'funaster', 'tatadocomo', 'sci', 'naylormarketing', 'payumoney', 'flickr', 'geeps', 'interviewbit', 'us', 'ames-it-solutions', 'repositoryhosting', 'imindmap', 'trigger', 'stackexchange', 'et', 'entropay', 'cs', 'pornhub', 'agencenavigo', 'tufinawatches', 'twenty19', 'astrospeak', 'comma', 'buffalo', 't', 'cbsnewsletter', 'divx', 'witai-2']

TLD_CATEGORIES = ['ebay.in', 'com', 'net', 'ac.in', 'bookmyshow.com', 'in', 'gov.in', 'fr', 'org', 'frankfurt-airport.news', 'sdconnect.in', 'google.com', 'pinterest.com', 'iitm.ac.in', 'grammarly.com', 'instagram.com', 'efinmail.com', 'surveymonkey.com', 'godaddy.com', 'foodpanda.in', 'co', 'gopro.com', 'lescrous.fr', 'goindigo.in', 'jabong.com', 'intercom-mail.com', 'speakingtree.in', 'paypal.com', 'mil', 'pytorch.org', 'netflix.com', 'asus.com', 'itunes.com', 'linkedin.com', 'bird.co', 'nvidia.com', 'mail.coursera.org', 'co.in', 'hp.com', 'travel-makemytrip.com', 'goodreads.com', 'mathworks.com', 'codeproject.com', 'ibm.com', 'wfp.org', 'payback.in', 'udacity.com', 'mobikwik.com', 'miscota.com', 'evernote.com', 'change.org', 'twitter.com', 'cardekhomailer.com', 'booking.com', 'travel2-makemytrip.com', 'ai', 'digitalglobe.com', 'hosting', 'skype.com', 'oneplus.com', 'tripadvisor.com', 'quoramail.com', 'emails-makemytrip.com', 'vincerowatches.com', 'mail.intercom.io', 'uber.com', 'vnet.ibm.com', 'xoom.com', 'org.in', 'classmates.com', 'cardekho.com', 'today', 'ibmmail.com', 'be', 'Apple.com', 'crazydomains.com', 'hobbyking.com', 'microsoft.com', 'email', 'ieee.org', 'info', 'last.fm', 'prezi.com', 'is', 'stanford.edu', 'ac.in', 'in', 'com', 'fr', 'foodpanda.in', 'org.in', 'ai', 'email', 'intercom-mail.com', 'gov.in', 'bookmyshow.com', 'asus.com', 'ebay.in', 'org', 'speakingtree.in', 'pinterest.com', 'supelec.fr', 'sdconnect.in', 'netflix.com', 'hp.com', 'google.com', 'grammarly.com', 'paypal.com', 'frankfurt-airport.news', 'net', 'orkut.com', 'mail.coursera.org', 'tripadvisor.com', 'bird.co', 'jabong.com', 'itunes.com', 'iiitd.ac.in', 'linkedin.com', 'co', 'godaddy.com', 'edu', 'ieee.org', 'auchan.net', 'goodreads.com', 'pytorch.org', 'co.in', 'cardekho.com', 'evernote.com', 'codeproject.com', 'nvidia.com', 'quoramail.com', 'travel-makemytrip.com', 'goindigo.in', 'udacity.com', 'gopro.com', 'io', 'centralesupelec.fr', 'reliancegeneral.co.in', 'mathworks.com', 'xoom.com', 'ibmmail.com', 'emails-makemytrip.com', 'wfp.org', 'instagram.com', 'classmates.com', 'twitter.com', 'skype.com', 'vincerowatches.com', 'Apple.com', 'asana.com', 'last.fm', 'cardekhomailer.com', 'efinmail.com', 'chtah.com', 'microsoft.com', 'vnet.ibm.com', 'scientific-direct.net', 'miscota.com', 'bitbucket.org', 'ORG', 'iitm.ac.in', 'elitmus.biz', 'booking.com', 'payback.in', 'surveymonkey.com', 'hobbyking.com', 'stanford.edu', 'ibm.com', 'tech', 'be']

def replaceNullsWithMode(fieldName, data):
	mode = data[fieldName].mode()[0]
	data[fieldName].fillna(mode, inplace=True)

def testResults(data):
	
## Read csvs

train_df = pd.read_csv('train.csv', index_col=0)
test_df = pd.read_csv('test.csv', index_col=0)

del train_df[DATE_FIELD]
del test_df[DATE_FIELD]

train_x, test_x, train_y, test_y = train_test_split(train_df, train_df[[LABEL_FIELD]], test_size=0.4)


replaceNullsWithMode(ORG_FIELD, train_x)
replaceNullsWithMode(TLD_FIELD, train_x)
replaceNullsWithMode(ORG_FIELD, test_x)
replaceNullsWithMode(TLD_FIELD, test_x)

columnTransformer = ColumnTransformer([("herpy derp", OneHotEncoder(categories=[ORG_CATEGORIES, TLD_CATEGORIES]), [ 0, 1, 4 ])], remainder='passthrough')

columnTransformer.fit(train_x)
train_x_featurized = columnTransformer.transform(train_x)
test_x_featurized = columnTransformer.transform(test_x)

## Train a simple KNN classifier using featurized data
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(train_x_featurized, train_y)
pred_y = neigh.predict(test_x_featurized)

## Save results to submission file
pred_df = pd.DataFrame(pred_y, columns=['label'])
pred_df.to_csv("knn_sample_submission", index=True, index_label='Id')

testResults(test_df)
