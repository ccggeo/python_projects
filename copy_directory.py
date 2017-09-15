from distutils.dir_util import copy_tree

# copy subdirectory. Uses copy_tree
fromDir = "/Volumes/CCSA_X64FRE_EN-US_DV5"
toDir = "/Users/cgeorge/desktop/ISO"
copy_tree(fromDir, toDir)


#http://pythoncentral.io/how-to-movecopy-a-file-or-directory-folder-with-a-progress-bar-in-python/