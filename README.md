# nicholsplotting
Simple Python script to plot bode diagrams on the 3D Nichols plot to assess closed-loop behaviour

## Based on
This script is based on the article in the IEEE Solid State Circuits Magazine (Vol. 14.2) by Chris Mangelsdorf: *Solving Tough Feedback Problems (Wihout Hair Loss)*

The article can be found on the IEEExplore: [https://doi.org/10.1109/MSSC.2022.3167301](https://doi.org/10.1109/MSSC.2022.3167301)"Solving Tough Feedback Problems (Without Hair Loss)"

Chris Mangelsdorf has published the MATLAB code upon which this is based to his github: [CMangelsdorf/SSCM](https://github.com/CMangelsdorf/SSCM/tree/main/SSCM/Spring_2022/Matlab)

## Usage Instructions

- Change the OL range to that of interest to suit your needs (such that your plot doesn't overshoot the Nichols surface)
- Specify your system loopgain equation for bode plotting
- Modify your frequency sweep as necessary to capture system dynamics
- This script should be easily modifiable if there is no transfer function model, but only bode plot data of the Loop Gain

## Example Data
A system with the loop gain illustrated in this bode plot:
![Example Bode Plot](/example_bodeplot.pdf)

is plotted on the nichols surface, with the following results:
![Example Nichols Plot](/example_nicholsplot.pdf)

Note that both positive __and negative frequencies__ were used to generate this plot.

Since the Nichols peak lies outside the area enclosed in the nichols contour, this example system is stable.