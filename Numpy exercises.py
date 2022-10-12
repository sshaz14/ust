{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eb955558",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "762f36b6",
   "metadata": {},
   "source": [
    "Ex1: Replace all odd/even number in given numpyarray with its negative"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6e47c94f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[49 39 12 26 38 13 43 46 17 43 17 44 35 12 44 43 49 43 46 23]\n",
      "[ 49  39 -12 -26 -38  13  43 -46  17  43  17 -44  35 -12 -44  43  49  43\n",
      " -46  23]\n"
     ]
    }
   ],
   "source": [
    "ex1=np.random.randint(10,50, size =(20))\n",
    "print(ex1)\n",
    "ex1[ex1 % 2 == 0] *= -1\n",
    "print(ex1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "46d1e830",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[33 27 26 44 31 17 11 26 46 26 42 28 49 15 12 40 37 23 24 28]\n",
      "[-33 -27  26  44 -31 -17 -11  26  46  26  42  28 -49 -15  12  40 -37 -23\n",
      "  24  28]\n"
     ]
    }
   ],
   "source": [
    "ex1=np.random.randint(10,50, size =(20))\n",
    "print(ex1)\n",
    "ex1[ex1 % 2 == 1] *= -1\n",
    "print(ex1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "faf25232",
   "metadata": {},
   "source": [
    "EX2: Create a numpy array from a csv file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "58961e07",
   "metadata": {},
   "outputs": [],
   "source": [
    "#read a .csv\n",
    "iris_data = np.genfromtxt('iris.csv', delimiter = ',', skip_header = 1,dtype = str, usecols=[0,1,2,3,4])\n",
    "#iris_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e5ea533",
   "metadata": {},
   "source": [
    "Ex3: Find the count of unique values in a numpy array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "dd9b95ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array(['setosa', 'versicolor', 'virginica'], dtype='<U10'),\n",
       " array([50, 50, 50], dtype=int64))"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris_data = np.genfromtxt('iris.csv', delimiter = ',', skip_header = 1,dtype = str, usecols=[4])\n",
    "np.unique(iris_data, return_counts=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "527e214e",
   "metadata": {},
   "source": [
    "Ex4: Filter numpy array based on two or more conditions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c1558bfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "iris_data = np.genfromtxt('iris.csv', delimiter = ',', skip_header = 1,dtype = float, usecols=[0,1,2,3])\n",
    "\n",
    "#iris_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "76b7b2f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[4.8, 3.4, 1.6, 0.2],\n",
       "       [4.8, 3.4, 1.9, 0.2],\n",
       "       [4.7, 3.2, 1.6, 0.2],\n",
       "       [4.8, 3.1, 1.6, 0.2],\n",
       "       [4.9, 2.4, 3.3, 1. ],\n",
       "       [4.9, 2.5, 4.5, 1.7]])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#3rd column is >1.5 and 1st column is <5.0\n",
    "iris_data[(iris_data[:, 2] > 1.5) & (iris_data[:, 0] < 5.0)]\n",
    "#iris_data[(iris_data[:, 2] > 1.5) & (iris_data[:, 0] < 5.5)]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb96cc28",
   "metadata": {},
   "source": [
    "EX5: Find if given array has Null/Nan values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "4b86bd4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.isnan(iris_data).any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "06ed94cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Replace values in col 2, 3.4 and 3rd colum, 1.7 ny np.nan\n",
    "iris_data[(iris_data[:,2] == 3.4)|(iris_data[:,3] == 1.7)]=np.nan\n",
    "#iris_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "226134cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.isnan(iris_data).any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "ee637782",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0, 12,  4,  2])"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# count of missing values\n",
    "np.isnan(iris_data).sum(axis=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45b19e83",
   "metadata": {},
   "source": [
    "Ex6: Find the most frequent value in a numpy arrayfor each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "891a7b0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n",
      "3.0\n",
      "1.4\n",
      "0.2\n"
     ]
    }
   ],
   "source": [
    "iris_data = np.genfromtxt('iris.csv', delimiter = ',', skip_header = 1, dtype = float, usecols=[0,1,2,3])\n",
    "for i in range(iris_data.shape[1]):\n",
    "    value, counts=np.unique(iris_data[:,i], return_counts=True)\n",
    "    print(value[np.argmax(counts)])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6e79918",
   "metadata": {},
   "source": [
    "Ex7: Find Index position of first occurance of a value greater than a given value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "d9be878f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "50\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "for i in range(iris_data.shape[1]):\n",
    "    print(np.argmax(iris_data[:, i] > 2.3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "aaa83749",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n",
      "[0]\n",
      "[50]\n",
      "[100]\n"
     ]
    }
   ],
   "source": [
    "for i in range(iris_data.shape[1]):\n",
    "    print(np.argwhere(iris_data[:, i] > 2.3)[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f66d871c",
   "metadata": {},
   "source": [
    "Ex8: Write a prog that accepts a sentence and find value counts of letter and digits. Iput will be supplied to prog"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "0b73363e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the sentence:jshfjfw758345\n",
      "Letters 7\n",
      "Digits 6\n"
     ]
    }
   ],
   "source": [
    "inp=input(\"Enter the sentence:\")\n",
    "dict1={'Letters':0, 'Digits':0}\n",
    "for char in inp:\n",
    "    if char.isdigit():\n",
    "        dict1['Digits']+=1\n",
    "    elif char.isalpha():\n",
    "        dict1['Letters']+=1\n",
    "    else:\n",
    "        pass\n",
    "print('Letters',dict1['Letters'])\n",
    "print('Digits',dict1['Digits'])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
