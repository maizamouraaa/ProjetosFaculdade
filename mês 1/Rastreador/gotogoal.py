import time
import numpy as np
import pycoppeliasim as sim
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Conectar ao CoppeliaSim
sim.simxFinish(-1)  # Fecha todas as conexões anteriores
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Inicia uma nova conexão

if clientID != -1:
    print('Conectado ao CoppeliaSim')
    
    # Handles dos objetos
    _, robot_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_blocking)
    _, goal_handle = sim.simxGetObjectHandle(clientID, '', sim.simx_opmode_blocking)
    _, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_blocking)
    _, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_blocking)

    # Pegar as posições iniciais
    sim.simxGetObjectPosition(clientID, robot_handle, -1, sim.simx_opmode_streaming)
    sim.simxGetObjectPosition(clientID, goal_handle, -1, sim.simx_opmode_streaming)
    sim.simxGetObjectOrientation(clientID, robot_handle, -1, sim.simx_opmode_streaming)

    base_speed = 2  # Velocidade base
    Kp = 0.5  # Ganho proporcional

    while True:
        # Posição do robô
        _, robot_position = sim.simxGetObjectPosition(clientID, robot_handle, -1, sim.simx_opmode_buffer)
        _, goal_position = sim.simxGetObjectPosition(clientID, goal_handle, -1, sim.simx_opmode_buffer)
        _, robot_orientation = sim.simxGetObjectOrientation(clientID, robot_handle, -1, sim.simx_opmode_buffer)

        dx = goal_position[0] - robot_position[0]
        dy = goal_position[1] - robot_position[1]

        angle_to_goal = np.arctan2(dy, dx)
        heading = robot_orientation[2]

        error = angle_to_goal - heading

        # Normalizar o erro angular
        if error > np.pi:
            error -= 2 * np.pi
        elif error < -np.pi:
            error += 2 * np.pi

        rotational_velocity = Kp * error

        # Ajustar velocidades dos motores
        sim.simxSetJointTargetVelocity(clientID, left_motor_handle, base_speed - rotational_velocity, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID, right_motor_handle, base_speed + rotational_velocity, sim.simx_opmode_streaming)

        time.sleep(0.1)
else:
    print('Falha na conexão com o CoppeliaSim')

sim.simxFinish(clientID)  # Fecha a conexão com o CoppeliaSim
