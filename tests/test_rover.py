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
    assert rover.position == (0, -1)
    
    # Face East, move backward
    rover.execute('R')  # now facing East
    rover.execute('B')
    assert rover.position == (-1, -1)

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