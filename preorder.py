#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pygame


# In[6]:


import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = pygame.font.SysFont("Arial", 30)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Binary Tree Traversal Game")

# Binary Tree Node Class
class Node:
    def __init__(self, data, pos):
        self.data = data
        self.left = None
        self.right = None
        self.pos = pos  # Position for visual representation

# Create binary tree
def create_tree():
    root = Node(1, (400, 100))
    root.left = Node(2, (250, 200))
    root.right = Node(3, (550, 200))
    root.left.left = Node(4, (150, 300))
    root.left.right = Node(5, (350, 300))
    root.right.left = Node(6, (450, 300))
    root.right.right = Node(7, (650, 300))
    return root

# Draw the binary tree
def draw_tree(node, visited_nodes):
    if node:
        pygame.draw.circle(screen, GREEN if node.data in visited_nodes else BLACK, node.pos, 30)
        pygame.draw.circle(screen, WHITE, node.pos, 28)
        text = FONT.render(str(node.data), True, BLACK)
        screen.blit(text, (node.pos[0] - 10, node.pos[1] - 15))
        if node.left:
            pygame.draw.line(screen, BLACK, node.pos, node.left.pos, 2)
            draw_tree(node.left, visited_nodes)
        if node.right:
            pygame.draw.line(screen, BLACK, node.pos, node.right.pos, 2)
            draw_tree(node.right, visited_nodes)

# Traversals
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        traversal_sequence.append(node.data)
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        traversal_sequence.append(node.data)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        traversal_sequence.append(node.data)

# Game loop
def game_loop():
    global traversal_sequence
    root = create_tree()
    visited_nodes = []
    node_map = {}  # For quick look-up of nodes
    for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]:
        node_map[node.data] = node

    # Choose a traversal type (e.g., Preorder)
    traversal_sequence = []
    preorder_traversal(root)
    traversal_index = 0

    running = True
    while running:
        screen.fill(WHITE)
        draw_tree(root, visited_nodes)

        # Display instruction
        instruction = FONT.render(f"Click nodes in Preorder: {traversal_sequence}", True, BLACK)
        screen.blit(instruction, (50, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # Check which node is clicked
                for node in node_map.values():
                    node_pos = node.pos
                    if ((event.pos[0] - node_pos[0]) ** 2 + (event.pos[1] - node_pos[1]) ** 2) ** 0.5 < 30:
                        if node.data == traversal_sequence[traversal_index]:
                            visited_nodes.append(node.data)
                            traversal_index += 1
                            if traversal_index == len(traversal_sequence):
                                print("You completed the traversal!")
                                pygame.quit()
                                sys.exit()

        pygame.display.update()

# Start game loop
game_loop()


# In[ ]:





# In[ ]:




