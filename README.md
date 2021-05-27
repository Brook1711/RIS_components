# RIS components
This is a python project for RIS(reconfigurable intelligent surface) simulations.

# related works
1. My first paper [Link to my paper](https://ieeexplore.ieee.org/document/9434412) / [Pdf to my paper](cite/Learning-based%20Robust%20and%20Secure%20Transmission%20forReconfigurable%20Intelligent%20Surface%20Aided%20MillimeterWave%20UAV%20Communications.pdf):
> [1] X. Guo, Y. Chen and Y. Wang, "Learning-based Robust and Secure Transmission for Reconfigurable Intelligent Surface Aided Millimeter Wave UAV Communications," in IEEE Wireless Communications Letters, doi: 10.1109/LWC.2021.3081464.

2. DDPG structure
> Refer to the following code on github:</br>
$\qquad$ a. [tf-agent](https://github.com/tensorflow/agents#Agents) this is the easiest way the use the official RL(reinforcement learning) api.</br>
$\qquad$ b. open source RL api using tensorflow: (coming soon)
$\qquad$ c. DDPG structure refters to [[3]](https://arxiv.org/abs/1509.02971)([pdf](cite/Continuous%20control%20with%20deep%20reinforcement%20learning.pdf)). There has already been some works on the combination of the DDPG and the RIS [[4]](https://arxiv.org/abs/2007.08380)([pdf](cite/Joint%20trajectory%20and%20passive%20beamforming%20design%20for%20intelligent%20reflecting%20surface-aided%20UAV%20communications%20A%20deep%20reinforcement%20learning%20approach.pdf)) 

1. RIS simulation 
Refer to the paper [Link to this paper](https://ieeexplore.ieee.org/document/9282349) / [Pdf to this paper](cite/SimRIS%20Channel%20Simulator%20for%20Reconfigurable%20IntelligentSurface-Empowered%20Communication%20Systems.pdf). This paper provide a simulation code in matlab, we refer to this project to provide a python version.
> [2] E. Basar and I. Yildirim, "SimRIS Channel Simulator for Reconfigurable Intelligent Surface-Empowered Communication Systems," 2020 IEEE Latin-American Conference on Communications (LATINCOM), 2020, pp. 1-6, doi: 10.1109/LATINCOM50620.2020.9282349.

# What this project aims ?
This project aims to redo the simulations shown in the paper below [Link to this paper](https://arxiv.org/abs/2103.15154):
> [3] Zhang, Zijian, et al. "Active RIS vs. Passive RIS: Which Will Prevail in 6G?." arXiv preprint arXiv:2103.15154 (2021).

Specifically, in this project we will simulate the active RIS. And to maximum the universality, this project will provide modular simulation tool for RIS-aided system.

# File structure
## ./cite
The cited paper for this project

## ./learning
The code to initialize the agents
### $\qquad$ ./learning/official
$\qquad$ The offical RL agents api ([tf-agent](https://github.com/tensorflow/agents#Agents))
### $\qquad$ ./learning/custom
$\qquad$ The third party open source RL agent api

# RIS theory
this section mainly refers to [2]. 
## RIS-Assisted LOS channels
According to the plate scattering theory[2,(1)], the transmitted signal is captured by each RIS element, then rescattered to the medium in all directions. Focusing on he $n$-th RIS element, the captured power on it can be readily obtained as
$$
P_{n}^{RIS}=\frac{P_tG_tG_E^{Tx}\lambda^2}{(4\pi)^2a_n^2}
\tag{1}
$$
where $P_t$ is the transmit power,$G_t$ is the transmit antenna gain in the direction of the $n$-th RIS element (or the RIS in general), $G_e^{Tx}$ is the gain of the corresponding RIS element in the direction of the transmitter (Tx), $\lambda$ is the wavelength, and $$

# Others
coding platform: Win10 pro, anaconda3

nvidia driver: 466.47

cuda version: cuda_11.1.1_456.81_win10

cuddn version: cudnn-11.2-windows-x64-v8.1.1.33

tensorflow version: 2.4.0

python version: 3.8.10
# Cited papers
[[1]](https://ieeexplore.ieee.org/document/9434412)([pdf](cite/Learning-based%20Robust%20and%20Secure%20Transmission%20forReconfigurable%20Intelligent%20Surface%20Aided%20MillimeterWave%20UAV%20Communications.pdf)) X. Guo, Y. Chen and Y. Wang, "Learning-based Robust and Secure Transmission for Reconfigurable Intelligent Surface Aided Millimeter Wave UAV Communications," in IEEE Wireless Communications Letters, doi: 10.1109/LWC.2021.3081464.

[2] E. Basar and I. Yildirim, "SimRIS Channel Simulator for Reconfigurable Intelligent Surface-Empowered Communication Systems," 2020 IEEE Latin-American Conference on Communications (LATINCOM), 2020, pp. 1-6, doi: 10.1109/LATINCOM50620.2020.9282349.

[[3]](https://arxiv.org/abs/1509.02971)([pdf](cite/Continuous%20control%20with%20deep%20reinforcement%20learning.pdf)) Lillicrap, Timothy P., et al. "Continuous control with deep reinforcement learning." arXiv preprint arXiv:1509.02971 (2015).

[[4]](https://arxiv.org/abs/2007.08380)([pdf](cite/Joint%20trajectory%20and%20passive%20beamforming%20design%20for%20intelligent%20reflecting%20surface-aided%20UAV%20communications%20A%20deep%20reinforcement%20learning%20approach.pdf)) Wang, Liang, et al. "Joint trajectory and passive beamforming design for intelligent reflecting surface-aided UAV communications: A deep reinforcement learning approach." arXiv preprint arXiv:2007.08380 (2020).