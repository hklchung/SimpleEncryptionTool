# SimpleEncryptionTool
###A simple encryption tool

In this project, I would like to explore using Principal Component Analysis (PCA) to 'encrypt' dataset and creating 'keys' that would allow the 'encrypted data' to be 'decrypted'.

According to GDPR Article 34, Section 3(a), data encryption frees data controllers from having to notify affected individuals about a personal data breach if the controller has implemented protection measures, “in particular those that render the personal data unintelligible to any person who is not authorised to access it, such as encryption.”

However there are two key concepts of encryption as outlined by the GDPR, namely anonymisation and pseudonymisation. In particular, anonymised data must be stripped of any identifiable information, making it impossible to derive insights on a discreet individual, even by the party that is responsible for the anonymisation.

On the otherhand, pseudonymisation refers to the processing of personal data in such a way that the data can no longer be attributed to a specific data subject without the use of additional information. This typically refers to personal identifiable information that is stored in separation and can only be constituted as personal data when presented in conjunction with information that allows for the identification of a natural person.

It is the goal of this project to create a novel methodology to encrypt personal data such that it can no longer be perceived as personal data by the GDPR.

###Methodology overview
First we need to transform all our data into numerical values. The only non-numerical data is the name, we will separate out the characters in the names and transform them according to their alphabetical orders, i.e. Bob → 2, 15, 2. (This can also be Ascii no.)
| Customer ID  | Name | Age | Salary |
| ------------ | ---- | --- | ------ |
| 1 | Bob | 30 | 15000 |
| 2 | Tom | 24 | 12000 |
| 3 | Ann | 44 | 23000 |
