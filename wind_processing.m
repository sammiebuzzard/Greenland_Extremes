% tried to do this in Python but still too novice
% need to load in Kap_Morris_2018 data
% interested in Wind heading and speed columns
% add requisite paths
% load requisite file

v = WND_SPD.*cos(WND_HD*pi/180); % calculating the meridional component of wind
v(v>100)=NaN; % eliminating fill values

%1 Feb - 28 Feb: 744:1413
%1 July - 31 Aug: 4290:5729

v_feb = v(744:1413);
v_Jul_Aug = v(4290:5729);
x_feb = [744/24,744/24];
y_feb = [-40,40];
x_Jul = [4290/24, 4290/24];
y_Jul = [-40,40];
x_Sep = [5729/24, 5729/24];
y_Sep = [-40,40];

t_feb = (1:length(v_feb))./24;
t_Jul_Aug = (1:length(v_Jul_Aug))./24;
t_all = (1:length(v))./24;

figure; plot(t_feb, v_feb); xlabel('Days from 1 Feb 2018 00:00'); ylabel('meridional component of wind, units unknown'); title('Feb meridional wind, Kap Morris')
figure; plot(t_Jul_Aug,v_Jul_Aug); xlabel('Days from 1 Jul 2018 00:00'); ylabel('meridional component of wind, units unknown'); title('Jul-Aug meridional wind, Kap Morris')

figure; plot(t_all,v); xlabel('Days from 1 Jan 2018'); ylabel('meridional component of wind, units unkn.')
hold on
plot(x_feb,y_feb,'LineWidth',3); plot(x_Jul,y_Jul,'LineWidth',3); plot(x_Sep,y_Sep,'LineWidth',3);
legend('meridional wind at Kap Morris','start of Feb','start of Jul','end of Aug');
title('Meridional wind at Kap Morris');