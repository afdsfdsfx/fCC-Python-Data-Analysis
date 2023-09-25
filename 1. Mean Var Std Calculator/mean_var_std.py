'''
Project No.: 1
Project Title: Mean-Variance-Standard Deviation Calculator
Date Completed: 2023-02-19



Instructions: 
    Create a function named calculate() that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

    The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

    The returned dictionary should follow this format:

        {
        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened]
        }

    If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

    For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

        {
        'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
        'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
        'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
        'max': [[6, 7, 8], [2, 5, 8], 8],
        'min': [[0, 1, 2], [0, 3, 6], 0],
        'sum': [[9, 12, 15], [3, 12, 21], 36]
        }

'''


# Importing necessary libraries
import numpy as np





# Creating the required function
def calculate(py_list):
	try:
		numpy_list = np.array(py_list).reshape((3, 3))
		
		stat_dic = {}
		
		stat_dic['mean'] = [
			numpy_list.mean(axis = 0).tolist(),
			numpy_list.mean(axis = 1).tolist(),
			numpy_list.mean().tolist()
			]
		
		stat_dic['variance'] = [
			numpy_list.var(axis = 0).tolist(),
			numpy_list.var(axis = 1).tolist(),
			numpy_list.var().tolist()
			]
		
		stat_dic['standard deviation'] = [
			numpy_list.std(axis = 0).tolist(),
			numpy_list.std(axis = 1).tolist(),
			numpy_list.std().tolist()
			]

		stat_dic['max'] = [
			numpy_list.max(axis = 0).tolist(),
			numpy_list.max(axis = 1).tolist(),
			numpy_list.max().tolist()
			]

		stat_dic['min'] = [
			numpy_list.min(axis = 0).tolist(), 
			numpy_list.min(axis = 1).tolist(),
			numpy_list.min().tolist()
			]

		stat_dic['sum'] = [
			numpy_list.sum(axis = 0).tolist(),
			numpy_list.sum(axis = 1).tolist(),
			numpy_list.sum().tolist()
			]

		return stat_dic

	except:
		raise ValueError('List must contain nine numbers.')