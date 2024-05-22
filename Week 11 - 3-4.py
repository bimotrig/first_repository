from sklearn import datasets, svm
import matplotlib

digits = datasets.load_digits()

#svm의 분류기 모델 SC를 학습
s = svm.SVC(gamma=0.1, C=10)
s.fit(digits.data, digits.target) #digits 데이터로 모델링

#consider and recognize the three samples in front of the training set as new raw flows
new_d = [digits.data[0], digits.data[1], digits.data[2]]
res = s.predict(new_d)
print("예측값은", res)
print("참값은", digits.target[0], digits.target[1], digits.target[2])

#recognize the training set as a test set and measure the accuracy rate
res = s.predict(digits.data)
correct = [i for i in range(len(res)) if res[i] == digits.target[i]]
accuracy = len(correct) / len(res)
print("화소 특징을 사용했을 때 정확도", accuracy * 100, "%")