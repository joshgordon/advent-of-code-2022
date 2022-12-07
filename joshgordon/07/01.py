#!/usr/bin/env python3

from typing import Optional
from enum import Enum

class Type(Enum):
    FILE = 0
    DIRECTORY = 1

class inode:
    name: str
    type: Type
    size: int
    children: dict[str, 'inode']
    parent: Optional['inode']

    def getRecursiveSize(self) -> int:
        return self.size + sum([child.getRecursiveSize() for child in self.children.values()])
    
    def getRecursivePath(self) -> str:
        path = []
        working = self
        if working.parent == None:
            return "/"
        else:
            while working:
                path.insert(0, working.name)
                working = working.parent
            return "/".join(path)

    def __str__(self):
        return f"inode: {self.getRecursivePath()}"



class FileInode(inode):
    def __init__(self, size, name, parent):
        self.size = size
        self.name = name
        self.children = {}
        self.type = Type.FILE
        self.parent = parent
    
    def getRecursiveSize(self) -> int:
        return self.size

class DirectoryInode(inode):
    def __init__(self, name: str, parent: inode, children: dict[str, inode] = {}):
        self.size = 0
        self.name = name
        self.children = children
        self.type = Type.DIRECTORY
        self.parent = parent

with open("example") as infile:
    cwd = []
    working_directory_inode = None
    while line := infile.readline():
        line = line.strip()

        if line[0] == "$":
            line = line.split(" ")[1:]
            if line[0] == "cd":
                if line[1] == "..":
                    cwd.pop()
                    working_directory_inode = working_directory_inode.parent
                elif line[1] == "/":
                    cwd = []

                    # make a new inode for /
                    slash = DirectoryInode("", None, {})
                    working_directory_inode = slash
                else:
                    cwd.append(line[1])
                    try:
                        working_directory_inode = working_directory_inode.children[line[1]]
                    except:
                        print(cwd, working_directory_inode)
            
            elif line[0] == "ls":
                lines = []
                while True:
                    # check the next char
                    chr = infile.read(1)
                    if chr == "":
                        break
                    else:
                        infile.seek(infile.tell() - 1)

                    if chr == "$": 
                        break

                    line = infile.readline().strip()
                    lines.append(line)
                
                for line in lines:
                    line = line.split(" ")
                    if line[0] == "dir": 
                        newdir = DirectoryInode(line[1], working_directory_inode)
                        working_directory_inode.children[line[1]] = newdir
                    else:
                        newfile = FileInode(int(line[0]), line[1], working_directory_inode)
                        working_directory_inode.children[line[1]] = newfile
                

import pdb
pdb.set_trace()


