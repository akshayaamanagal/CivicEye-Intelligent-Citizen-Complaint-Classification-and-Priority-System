from CivicEyeSBERT.predict_service import predict_complaint

text ="Live electric wire fallen on the road after rain."

result = predict_complaint(text)
print(result)

