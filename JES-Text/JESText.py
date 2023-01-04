def textOnImage():
  file = pickAFile()
  pic = makePicture(file)
  str = "This is a test."
  addText(pic, 50, 50, str)
  addText(pic, 100, 100, str, blue)
  show(pic)
  
def StyledTextOnImage():
  import java.awt.Font as Font
  file = pickAFile() 
  pic = makePicture(file)
  str = "This is a test."
  myFont = makeStyle("Arial", Font.BOLD, 64)
  addTextWithStyle(pic, 50, 50, str, myFont)
  addTextWithStyle(pic, 100, 100, str, myFont, blue)
  show(pic)