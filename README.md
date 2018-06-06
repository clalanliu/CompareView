# CompareView

> A concise image viewer for image comparison.   
![image](https://github.com/yan88663319/CompareView/blob/master/icon/intGif.gif)

**Key features:**

* Convenient to switch compared images by arrow keys or mouse wheel!
* Easy to reload images by pressing spacebar.
* Support for multiple images.
* Enlarge where you want.
* Quick MSE, PSNR, SSIM evaluation.

**Steps:**  

* Install necessary packages first (python3.5 needed):  
  ```bash
	pip install numpy pillow scipy scikit-image
	```

* To run the program:
  ```bash
	python CompairView.pyw
	```

* To build the executable file:
  ```bash
	pyinstaller -F CompairView.pyw
	```

**Usage:**
* Arrow key and mouse wheel: Switch image.
* Del: Delete the image.
* R/r: Reload all images.
* Box out the rectangle and press z/Z: Enlarge the wanted region.
* Number key: Zoom in the image with the same region of the other image.
* Double click: Zoom out to the origin one.  


(Window maximizing button is unsupported for the present and hence maximizing the window will result in unexpected error! Please resize the window by the mouse if needed.)
