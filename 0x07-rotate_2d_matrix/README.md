## ROTATE 2D MATRIX
A <strong>2D matrix rotation</strong> is the process of rotating the elements of a matrix by <strong>90 degrees in a clockwise or anti-clockwise direction.</strong> This operation can be performed on a square matrix (where the number of rows and columns are equal) to achieve the desired rotation.
<br>
To rotate a 2D matrix, we will use a common method called the "transpose and reverse" technique, which involves the following steps:
<br>
<ol>
<li>Transpose the Matrix: To transpose a matrix, we need to swap its rows with columns. For each element in the matrix, swap its row index with its column index. This means that we exchange the position of an element in terms of its row and column within the matrix. This operation effectively reflects the matrix along its main diagonal.</li>
<br>
<li>Reverse Each Row: After transposing the matrix, reverse the elements of each row. This can be achieved by swapping the elements at the leftmost and rightmost positions, then moving inward towards the center until all elements have been swapped.</li>
</ol>
<br>
By performing these two steps, the matrix will be rotated by 90 degrees in a clockwise direction. If we want to rotate it anti-clockwise, we can perform the reverse operation, i.e., reverse each row first and then transpose the matrix.
<br>
For instance, if we have a 4x4 matrix below:<br>
	<p style="text-align: center;">[[1, 2, 3, 4]
	 [5, 6, 7, 8]
	 [9, 10, 11, 12]
	 [13, 14, 15, 16]] </p>
<br>
We can transpose and reverse it like this:<br>
	<p style="text-align: center;">[[1, 5, 9, 13]
	 [2, 6, 10, 14]
	 [3, 7, 11, 15]
	 [4, 8, 12, 16]]</p>
<br>
The above example is what we refer to as a matrix being edited in-place. For a matrix to be edited in place it means that the original or given matrix is being modified directly without creating a new one which in turn occupy the same memory space as the original matrix.
<br>
<h2 style="color: blue; font-family: sans-serif; font-weight: bold;">CONCLUSION</h2>
In conclusion, 2D Mtrix Rotation cannot be applied to a non-square matrix because of the follow:<br>
<ol>
<li>In the transposition step, the rows of the matrix are swapped with the corresponding columns. This operation assumes that the matrix has an equal number of rows and columns. If the matrix is non-square, the transposition would not be possible without changing the dimensions of the matrix.</li>
<br>
<li>Similarly, when reversing the rows, the assumption is that all rows have the same length. If the matrix is non-square, the row lengths may differ, and reversing rows would not be a valid operation.</li>
</ol>
