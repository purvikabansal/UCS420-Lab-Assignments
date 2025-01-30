# Q5
ucs420_purvika = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print(ucs420_purvika.mean(), np.median(ucs420_purvika), ucs420_purvika.max(), ucs420_purvika.min(), np.unique(ucs420_purvika))
reshaped_ucs420_purvika = ucs420_purvika.reshape(4, 3)
resized_ucs420_purvika = reshaped_ucs420_purvika[:2, :3]
print(reshaped_ucs420_purvika)
print(resized_ucs420_purvika)
