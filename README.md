# Simple Encryption Tool ![Key](https://media.istockphoto.com/vectors/hand-drawn-antique-key-sketch-style-of-vintage-key-on-white-old-vector-id895217258){:height="24px" width="48px"}
## Introduction

In this project, I would like to explore using Principal Component Analysis (PCA) to 'encrypt' dataset and creating 'keys' that would allow the 'encrypted data' to be 'decrypted'.

According to GDPR Article 34, Section 3(a), data encryption frees data controllers from having to notify affected individuals about a personal data breach if the controller has implemented protection measures, “in particular those that render the personal data unintelligible to any person who is not authorised to access it, such as encryption.”

However there are two key concepts of encryption as outlined by the GDPR, namely anonymisation and pseudonymisation. In particular, anonymised data must be stripped of any identifiable information, making it impossible to derive insights on a discreet individual, even by the party that is responsible for the anonymisation.

On the otherhand, pseudonymisation refers to the processing of personal data in such a way that the data can no longer be attributed to a specific data subject without the use of additional information. This typically refers to personal identifiable information that is stored in separation and can only be constituted as personal data when presented in conjunction with information that allows for the identification of a natural person.

It is the goal of this project to create a novel methodology to encrypt personal data such that it can no longer be perceived as personal data by the GDPR.

## Methodology overview
###### Original dataset
| Customer ID  | Name | Age | Salary |
| ------------ | ---- | --- | ------ |
| 1 | Bob | 30 | 15000 |
| 2 | Tom | 24 | 12000 |
| 3 | Ann | 44 | 23000 |

First we need to transform all our data into numerical values. The only non-numerical data is the name, we will separate out the characters in the names and transform them according to their alphabetical orders, i.e. Bob → 2, 15, 2. (This can also be Ascii no.)
###### Transformed dataset
| Customer ID  | Name_char1 | Name_char2 | Name_char3 | Age | Salary |
| ------------ | ---------- | ---------- | ---------- | --- | ------ |
| 1 | 2 | 15 | 2 | 30 | 15000 |
| 2 | 20 | 15 | 13 | 24 | 12000 |
| 3 | 1 | 14 | 14 | 44 | 23000 |

We apply principal component analysis to compute eigenvectors of the covariance matrix. This will then result in ‘scrambled’ data. In practice, this is the original dataset with 'dimensionality reduced' but without data loss as no. of PCs is identical to no. of columns in the original dataset.
###### New dataset
| C1  | C2 | C3 |
| --- | -- | -- |
| -1.66666216e+03 | 1.06829921e+01 | -2.38031816e-13 |
| -4.66668575e+03 | -7.76943478e+00 | -2.27817765e-13 |
| 6.33334791e+03 | -2.91355728e+00 | 4.67847983e-13 |

The new data set can then be stored and transferred freely as non-personal data. To reverse the data set, one must have the 'key'. The 'key' was created during dimensionality reduction and captured as
- 'mu', per-feature empirical mean that was estimated from the original dataset, and 
- 'key', the principal axes in feature space, representing the directions of maximum variance in the data. The components are sorted by their explained variance.

Imagine lauching nuclear missiles from a submarine, we need two keys to reverse the 'encrypted' data back to the original dataset. To do this, we use the following formula: encrypted data ⋅ Transpose(eigenvectors) + Mean, where Transpose(eigenvectors) = key and Mean = mu. It is important to note that any slight changes to key or mu will result in inability to reconstruct the original dataset. 

## Future updates
- Automated parsing of string type columns
- Packaging of 'encrypted data' with 'key'
