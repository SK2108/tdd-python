import pytest
from python_starter.rover import Rover

def test_rover_initial_position():
    rover = Rover()
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'

def test_rover_turn_left():
    rover = Rover()
    rover.execute('L')
    assert rover.orientation == 'W'
    rover.execute('L')
    assert rover.orientation == 'S'
    rover.execute('L')
    assert rover.orientation == 'E'
    rover.execute('L')
    assert rover.orientation == 'N'

def test_rover_turn_right():
    rover = Rover()
    rover.execute('R')
    assert rover.orientation == 'E'
    rover.execute('R')
    assert rover.orientation == 'S'
    rover.execute('R')
    assert rover.orientation == 'W'
    rover.execute('R')
    assert rover.orientation == 'N'

def test_rover_move_forward():
    rover = Rover()
    # Face North, move forward
    rover.execute('F')
    assert rover.position == (0, 1)
    
    # Face East, move forward
    rover.execute('R')  # now facing East
    rover.execute('F')
    assert rover.position == (1, 1)

def test_rover_move_backward():
    rover = Rover()
    # Face North, move backward
    rover.execute('B')
    assert rover.position == (0, 9)  # Wraps to bottom of grid
    
    # Face East, move backward
    rover.execute('R')  # now facing East
    rover.execute('B')
    assert rover.position == (9, 9)  # Wraps to left edge

def test_rover_complex_movement():
    rover = Rover()
    # Test sequence: FFRFFLF (forward, forward, right, forward, forward, left, forward)
    rover.execute('FFRFFLF')
    assert rover.position == (2, 3)
    assert rover.orientation == 'N'

def test_rover_forward_backward():
    rover = Rover()
    # Test moving forward then backward returns to start
    rover.execute('FB')
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'
    
    # Test moving in a square pattern
    rover.execute('FRFRFRFR')  # Should make a complete square and return to start
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'

def test_rover_double_forward():
    rover = Rover()
    # Test that FF moves from (0,0) to (0,2)
    rover.execute('FF')
    assert rover.position == (0, 2)
    assert rover.orientation == 'N'  # Orientation should remain North

def test_rover_turn_move_turn():
    rover = Rover()
    # Starting at (0,0) facing North
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'
    
    # Execute RFR: turn right, move forward, turn right
    rover.execute('RFR')
    
    # Should be at (1,0) facing South
    assert rover.position == (1, 0)
    assert rover.orientation == 'S'

def test_rover_wrap_around_north():
    rover = Rover()
    # Move forward 10 times facing north
    rover.execute('F' * 10)
    # Should wrap back to starting y position
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'

def test_rover_wrap_around_east():
    rover = Rover()
    # Turn right to face east, then move forward 12 times
    rover.execute('R' + 'F' * 12)
    # Should wrap to x=2 (as 12 % 10 = 2)
    assert rover.position == (2, 0)
    assert rover.orientation == 'E'

def test_rover_wrap_around_negative():
    rover = Rover()
    # Move backward 3 times while facing north (equivalent to going south)
    rover.execute('B' * 3)
    # Should wrap to y=7 (as -3 % 10 = 7)
    assert rover.position == (0, 7)
    assert rover.orientation == 'N'

def test_rover_wrap_around_diagonal():
    rover = Rover()
    # Move diagonally across the grid with wrapping
    rover.execute('F' * 15 + 'R' + 'F' * 15)
    # Should be at (5, 5) after wrapping both coordinates
    assert rover.position == (5, 5)
    assert rover.orientation == 'E'