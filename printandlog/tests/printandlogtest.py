from unittest import TestCase
import printandlog
import re
import os

class Test_printandlogtest(TestCase):
  def test_file_name(self):
    filePath = printandlog.makeUniqueFileName("CompareFolders.txt")
    dirName = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    self.assertEquals(dirName, printandlog.defaultFolder())
    reFileName = re.compile('CompareFolders_\d\d\d\d_\d\d_\d\d_\d\d_\d\d_\d\d\.txt')
    self.assertIsNotNone(reFileName.match(fileName))

  def test_file_path(self):
    initialFilePath = "D:\Log\Log\CompareFolders.txt"
    initialDirName = os.path.dirname(initialFilePath)
    filePath = printandlog.makeUniqueFileName(initialFilePath)
    dirName = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    self.assertEquals(dirName, initialDirName)
    reFileName = re.compile('CompareFolders_\d\d\d\d_\d\d_\d\d_\d\d_\d\d_\d\d\.txt')
    self.assertIsNotNone(reFileName.match(fileName))

if __name__ == '__main__':
    unittest.main()


