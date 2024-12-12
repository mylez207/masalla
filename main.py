import streamlit as st
import numpy as np

# Set up the page layout and title
st.set_page_config(page_title="NumPy Assignment Solutions", layout="wide")
st.title('NumPy Assignment Solutions')

st.markdown("""
GROUP MEMBERS \n\n
MASALA MASHAURI EASTC/BDTS/23/00176 \n
IRENE J BUSHIRI EASTC/BDTS/23/00189 \n
KASIMU CHAMBULILO EASTC/BDTS/23/00399\n
GERLAD K SHAYO EASTC/BDTS/23/00335\n
DANIEL SELESTINE EASTC/BDTS/23/00194\n
ABEL MBOGO EASTC/BDTS/23/00160\n
""")

# Add some introductory text
st.markdown("""
This app displays the solutions to the NumPy assignment. 
You will find each question's answer along with the Python code used to generate the solution.
""")

# Function to display code block in markdown style
def display_code(code):
    st.code(code, language='python')

# Question 1
st.header("**Question 1**: Create a 3x3 matrix containing integers from 1 to 9.")

# a. Create the matrix
matrix_3x3 = np.arange(1, 10).reshape(3, 3)
code_q1 = '''# Create a 3x3 matrix containing integers from 1 to 9
matrix_3x3 = np.arange(1, 10).reshape(3, 3)
'''

# b. Print the shape, size, and data type
shape = matrix_3x3.shape
size = matrix_3x3.size
dtype = matrix_3x3.dtype

st.subheader("Matrix:")
st.write(matrix_3x3)
display_code(code_q1)

st.subheader("Shape:")
st.write(shape)

st.subheader("Size:")
st.write(size)

st.subheader("Data Type:")
st.write(dtype)

# Question 2
st.header("**Question 2**: Create a 5x5 matrix with values from 1 to 25 and extract data.")

# a. Create the matrix
matrix_5x5 = np.arange(1, 26).reshape(5, 5)
code_q2 = '''# Create a 5x5 matrix with values from 1 to 25
matrix_5x5 = np.arange(1, 26).reshape(5, 5)
'''

# Extract:
first_row = matrix_5x5[0, :]
last_column = matrix_5x5[:, -1]
center_submatrix = matrix_5x5[1:3, 1:3]

st.subheader("Matrix:")
st.write(matrix_5x5)
display_code(code_q2)

st.subheader("First Row:")
st.write(first_row)

st.subheader("Last Column:")
st.write(last_column)

st.subheader("Center 2x2 Sub-Matrix:")
st.write(center_submatrix)

# Question 3
st.header("**Question 3**: Perform arithmetic operations on two 1D arrays.")

# a. Create arrays a and b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
code_q3 = '''# Create two 1D arrays: a = [1, 2, 3] and b = [4, 5, 6]
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
'''

# b. Compute the operations
elementwise_addition = a + b
dot_product = np.dot(a, b)
elementwise_multiplication = a * b

st.subheader("Element-wise Addition:")
st.write(elementwise_addition)

st.subheader("Dot Product:")
st.write(dot_product)

st.subheader("Element-wise Multiplication:")
st.write(elementwise_multiplication)

display_code(code_q3)

# Question 4
st.header("**Question 4**: Reshape and Flatten a 1D array.")

# a. Create a 1D array
array_1d = np.arange(1, 13)
code_q4 = '''# Create a 1D array of 12 elements from 1 to 12
array_1d = np.arange(1, 13)
'''

# b. Reshape the array into a 3x4 matrix
reshaped_matrix = array_1d.reshape(3, 4)
# c. Flatten the matrix
flattened_array = reshaped_matrix.flatten()

st.subheader("1D Array:")
st.write(array_1d)

st.subheader("Reshaped 3x4 Matrix:")
st.write(reshaped_matrix)

st.subheader("Flattened Array:")
st.write(flattened_array)

display_code(code_q4)

# Question 5
st.header("**Question 5**: Compute statistics on random integers.")

# a. Create random integers
random_integers = np.random.randint(1, 101, 10)
code_q5 = '''# Create an array of 10 random integers between 1 and 100
random_integers = np.random.randint(1, 101, 10)
'''

# b. Compute statistics
mean = np.mean(random_integers)
median = np.median(random_integers)
std_dev = np.std(random_integers)

st.subheader("Random Integers:")
st.write(random_integers)

st.subheader("Mean:")
st.write(mean)

st.subheader("Median:")
st.write(median)

st.subheader("Standard Deviation:")
st.write(std_dev)

display_code(code_q5)

# Question 6
st.header("**Question 6**: Extract elements greater than 30.")

# a. Create an array
array_6_elements = np.array([10, 20, 30, 40, 50, 60])
code_q6 = '''# Create an array: [10, 20, 30, 40, 50, 60]
array_6_elements = np.array([10, 20, 30, 40, 50, 60])
'''

# b. Extract elements greater than 30
elements_greater_than_30 = array_6_elements[array_6_elements > 30]

st.subheader("Array:")
st.write(array_6_elements)

st.subheader("Elements Greater Than 30:")
st.write(elements_greater_than_30)

display_code(code_q6)

# Add some final styling and note
st.markdown("""
### Thank you for reviewing the assignment solutions.
This app demonstrates the use of NumPy for various matrix operations and statistical computations. 
Feel free to explore and experiment with the code!
""")
