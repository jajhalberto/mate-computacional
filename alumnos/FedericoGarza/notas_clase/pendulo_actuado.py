
class Pendulo_actuado:
    
    def __init__(self, masa, longitud, gravedad, beta, A, f):
        self.masa = masa
        self.longitud = longitud
        self.gravedad = gravedad
        self.beta = beta
        self.A = A
        self.f = f
      
        self.Omega = sqrt(g/longitud)
        self.period = 2*np.pi/Omega

        
    def theta(self):
        return self.trajectory[:,0]
    
    def omega(self):
        return self.trajectory[:,1]
    
    def plot(self):
        fig, ax = plt.subplots(3,1, figsize=(10,8), sharex = True)

        ax[0].plot(self.tau, self.theta(), label="theta", color="blue")
        ax[1].plot(self.tau, self.omega(), label="omega", color="green")
        ax[2].plot(self.tau, self.energy(),  marker='o', linestyle='None', color='red', label="Energia")

        ax[0].set_ylabel("Theta (rads)")
        ax[0].set_xlabel("tiempo (s)")

        ax[1].set_ylabel("Omega (rads/s)")
        ax[1].set_xlabel("tiempo (s)")

        ax[2].set_ylabel("Energia (J)")
        ax[2].set_xlabel("tiempo (s)")
    
    def initial_conditions(self, theta_i, omega_i):
        self.theta_i = theta_i
        self.omega_i = omega_i
        
    def dynamics(self, state, t):
        g0 = state[1]
        g1 = -self.gravedad/self.longitud*np.sin(state[0]) - self.beta*slef.theta + A*np.cos(self.f*t)
        return np.array([g0, g1])
        
    def energy(self):
        return 0.5*self.masa*(self.longitud**2)*(self.omega()**2) + self.masa*self.gravedad*self.longitud*(1-np.cos(self.theta()))
        
    def integrate(self, num_steps, t_i, t_f, method):
        
        self.tau, self.dt = np.linspace(t_i, t_f, num=num_steps, retstep=True)
        self.trajectory = np.zeros([num_steps, 2])
        self.trajectory[0,0] = self.theta_i
        self.trajectory[0,1] = self.omega_i
        
        for j in range(num_steps-1):
            self.trajectory[j+1] = method(self.trajectory[j], self.tau[j], self.dt, self.dynamics) 
            
    def diagrama_de_fase(self):
        plt.plot(self.theta(), self.omega())
        plt.xlabel("theta (rads)")
        plt.ylabel("omega (rads/s)")
    