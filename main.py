# Access multiple elements in List by their indices in Python

a_list = ['bobby', 'hadz', 'com', 'a', 'b', 'c']

indices = [0, 2, 4]

# ✅ using a list comprehension

new_list = [a_list[index] for index in indices]
print(new_list)  # 👉️ ['bobby', 'com', 'b']