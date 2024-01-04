# globals.py
import pygame
from constants import WIDTH, HEIGHT, BG_COLOR

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)
