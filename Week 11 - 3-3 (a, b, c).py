from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset
digits = datasets.load_digits()

# Plot the first digit image
plt.figure(figsize=(5, 5))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

# Print the data of the first digit
print(digits.data[0])
print("이 숫자는", digits.target[0], "입니다")

# Load the LFW (Labeled Faces in the Wild) dataset
lfw = datasets.fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# Plot the first 8 faces from the LFW dataset
plt.figure(figsize=(20, 5))
for i in range(8):
    plt.subplot(1, 8, i + 1)
    plt.imshow(lfw.images[i], cmap=plt.cm.bone)
    plt.title(lfw.target_names[lfw.target[i]])

plt.show()

# Load the 20 newsgroups dataset
news = datasets.fetch_20newsgroups(subset='train')

# Print the first document and its class
print("*****\n", news.data[0], "\n*****")
print("The class of this document is <", news.target_names[news.target[0]], ">")
