from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import time
client = RemoteAPIClient()
sim = client.getObject('sim')
print("Iniciando simula??o...")
sim.startSimulation()
#motores
RodaD2 = sim.getObject('/direita')
RodaE2 = sim.getObject('/esquerda')
print("Motores obtidos com sucesso.")
L = 0.172 # distancia das rodas
r = 0.065 # raio das rodas
v = 0.2 # velocidade linear
w = 0 # velocidade linear
wr = ((2.0 * v) + (w * L)) / (2.0 * r)
wl = ((2.0 * v) - (w * L)) / (2.0 * r)
print(f"Velocidade angular da roda direita (wr): {wr}")
print(f"Velocidade angular da roda esquerda (wl): {wl}")
sim.setJointTargetVelocity(RodaD2, wr)
sim.setJointTargetVelocity(RodaE2, wl)
print("Velocidades definidas com sucesso.")
time.sleep(5)
chegada = chegada + 1 
if chegada == 0:
    handle_goal = sim.getObject("/Ponto1")
    pos_goal = sim.getObjectPosition(handle_goal,-1)
    theta_goal = sim.getObjectOrientation(handle_goal,-1)[2]

vel_esq = sim.setJointTargetVelocity(RodaE2, 0)
vel_dir = sim.setJointTargetVelocity(RodaD2, 0)

sim.stopSimulation()
