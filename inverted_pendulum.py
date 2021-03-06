import numpy as np
import matplotlib.pyplot as plt
"""
    Adaptative PD controler for inverted pendulum
"""

def draw_pendulum(l = 0.1,tht_i = 0):
    
    
    # Get coords
    x_coord = l*np.cos(tht_i)
    y_coord = l*np.sin(tht_i)

    #Circle
    theta = np.linspace( 0 , 2 * np.pi , 150 )
    rad = 0.2
    a = rad * np.cos( theta ) + x_coord
    b = rad * np.sin( theta ) + y_coord
    plt.figure("animation")
    plt.clf()
    plt.gcf().canvas.mpl_connect(
    'key_release_event',
    lambda event: [exit(0) if event.key == 'escape' else None])
    plt.plot(a, b)
    plt.xlim(-2,2)
    plt.ylim(-2,2)


    # Line
    plt.plot([0, x_coord], [0, y_coord])
    plt.pause(0.00001)
    plt.ion()
    



def main():
    
    # desired position
    th_des = (np.pi)/2

    # neuron weights ( these will be the control gains kp, kd  respectively)
    w_1 = 4.0
    w_2 = 0.0

    # Learning Factor
    eta_1 = 0.01
    eta_2 = 0.1

    # error auxiliar
    e_old = 0

    # sampling time, seconds, number of iterations
    t = 0.01
    s = 50
    n = int(s/t)

    # initial position and velocity
    th_i = (np.pi)/4 + 0.05 * 0
    thd_i = 0.0

    # pendulum parameters (mass, length, gravity, friction coefficient  respectively)
    m = 0.5
    l = 0.85
    g = 9.81
    B = 0.02

    # for plotting
    th_des_plot = np.zeros(n)
    th_i_plot = np.zeros(n)
    ctrl_plot = np.zeros(n)  
    gain_plot =  np.zeros((2,n))  

    for i in range(0,n):
        draw_pendulum(l,th_i)
        e = th_des - th_i

        x_1 = e #P
        x_2 = (e - e_old)/t #D

        e_old = e

        # control action
        u = x_1*w_1 + x_2*w_2

        #System
        thdd_i = u/(m*l**2) - (g/l)*np.cos(th_i) - B/(m*l**2)*thd_i
        thd_i = thd_i + thdd_i*t
        th_i = th_i + thd_i*t + 0.5*thdd_i*t**2

        # Update weights 
        w_1 = w_1 + eta_1*u*x_1
        w_2 = w_2 + eta_2*u*x_2

        if w_1 < 0:
            w1 = 0
        if w_2 < 0:
            w2 = 0

        th_des_plot[i] = th_des
        th_i_plot[i] = th_i
        ctrl_plot[i] = thdd_i
        gain_plot[0,i] = w_1
        gain_plot[1,i] = w_2


    t_plot = np.arange(t,s+t,t)

    plt.figure()
    plt.grid(True)
    plt.plot(t_plot,th_des_plot,label = 'Desired position')
    plt.plot(t_plot,th_i_plot, label = 'Position')
    plt.title("Angular control position")
    plt.xlabel("Time (secs)")
    plt.ylabel("Angular position (rad)")
    plt.legend()

    plt.figure()
    plt.grid(True)
    plt.plot(t_plot,ctrl_plot)
    plt.title("Control action")
    plt.xlabel("Time (secs)")
    plt.ylabel("Angular acceleration (rad/s^2)")

    plt.figure()
    plt.grid(True)
    plt.plot(t_plot,gain_plot[0,:], label='w_1 (k_p)')
    plt.plot(t_plot,gain_plot[1,:], label='w_2 (k_d)')
    plt.title("Gains")
    plt.xlabel("Time (secs)")
    plt.ylabel("Gain value)")
    plt.legend()

    plt.show()



if __name__ == "__main__":
    main()
    

