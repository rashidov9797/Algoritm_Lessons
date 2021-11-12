# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:31:33 2021

@author: rashi
"""

class Stack:
    """Stack obyekti"""
    def __init__(self):
        self.stack = []
        
    def isEmty(self):
        """Bo'sh emasligini tekshirish"""
        return len(self.stack)==0
    
    def push(self,data):
        """Element qo'shish"""
        self.stack.append(data)
    def pop(self):
        """Element sug'urib olish"""
        if self.isEmty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmty():
            """Stack is empty"""
        else:
            return self.stack[-1]