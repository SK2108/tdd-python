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
    # Face East, move backward
    rover.execute('R')  # face East
    rover.execute('B')
    assert rover.position == (9, 0)  # Wraps horizontally only
    
    # Return to start
    rover.execute('F')
    assert rover.position == (0, 0)
    
    # Face North, move backward through South pole
    rover.execute('L')  # face North
    rover.execute('B' * 10)  # Move through South pole
    # Position should be on the opposite longitude, at the bottom of the sphere
    assert rover.position == (5, 9)  
    # Orientation flips when crossing pole
    assert rover.orientation == 'S'

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
    # Move forward through North pole
    rover.execute('F' * 10)
    # Should appear on opposite side facing South
    assert rover.position == (5, 9)
    assert rover.orientation == 'S'

def test_rover_wrap_around_east():
    rover = Rover()
    # Turn right to face east, then move forward 12 times
    rover.execute('R' + 'F' * 12)
    # Should wrap to x=2 (as 12 % 10 = 2)
    assert rover.position == (2, 0)
    assert rover.orientation == 'E'  # Direction unchanged for E/W wrapping

def test_rover_wrap_around_poles():
    rover = Rover()
    # Move through North pole, then South pole
    rover.execute('F' * 20)
    # Should be back at original position with original orientation
    assert rover.position == (0, 0)
    assert rover.orientation == 'N'

def test_rover_wrap_around_diagonal():
    rover = Rover()
    # Move North until crossing pole
    rover.execute('F' * 10)
    # After crossing North pole, should be at longitude 5, facing South
    assert rover.position == (5, 9)
    assert rover.orientation == 'S'
    
    # Continue moving "North" (now South from other side) for 5 more steps
    rover.execute('F' * 5)
    # Should have moved 5 steps down from top
    assert rover.position == (5, 4)
    assert rover.orientation == 'S'
    
    # Turn right to face West and move
    rover.execute('R' + 'F' * 15)
    # Position should stay at same y, x should wrap normally
    assert rover.position == (5, 4)
    assert rover.orientation == 'W'

def test_rover_cross_north_pole():
    rover = Rover()
    # Start at (2,0) facing North
    rover.execute('R' + 'F' * 2 + 'L')  # Move to (2,0)
    assert rover.position == (2, 0)
    assert rover.orientation == 'N'
    
    # Move across North pole
    rover.execute('F' * 10)
    # Should appear on opposite longitude (2 + 5 = 7), at the top of the sphere
    assert rover.position == (7, 9)
    assert rover.orientation == 'S'

def test_rover_cross_south_pole():
    rover = Rover()
    # Start at (3,0) facing South
    rover.execute('R' + 'F' * 3 + 'R')  # Move to (3,0)
    assert rover.position == (3, 0)
    assert rover.orientation == 'S'
    
    # Move across South pole
    rover.execute('F' * 10)
    # Should appear on opposite longitude (3 + 5 = 8), at the bottom of the sphere
    assert rover.position == (8, 9)
    assert rover.orientation == 'N'

def test_rover_pole_crossing_multiple():
    rover = Rover()
    # Cross pole multiple times
    rover.execute('F' * 20)  # Cross North pole twice
    # Should be back at original longitude, facing original direction
    assert rover.position[0] == 0  # Same x coordinate
    assert rover.orientation == 'N'

def test_rover_backward_pole_crossing():
    rover = Rover()
    # Move to (4,0) facing North
    rover.execute('R' + 'F' * 4 + 'L')
    # Cross pole backward
    rover.execute('B' * 10)
    # Should appear on opposite longitude (4 + 5 = 9), at the bottom of the sphere
    assert rover.position == (9, 9)
    assert rover.orientation == 'S'