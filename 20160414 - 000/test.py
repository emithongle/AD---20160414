# from libs.features import getFeatureNames, preprocess, feature
#
# def printData(text):
#     print('Text : ', text)
#     for i, j in zip(getFeatureNames(), feature(preprocess(text))):
#         print(i, ' : ', j)
#     print('---------------------------------')
#
# printData('q 10')
# printData('qua 3')



from libs.segment import templateSegment

print(templateSegment('a b c d e', 2))
print(templateSegment('a b c d e', 3))
print(templateSegment('a b c d e', 4))