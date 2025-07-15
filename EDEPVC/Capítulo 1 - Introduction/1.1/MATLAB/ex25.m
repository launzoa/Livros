% Questão 25, equação y' = -{2t+y}/{2y}

% Definindo o campo de direções
[T, Y] = meshgrid(0:0.5:10, -10:1:10);

% Definindo a equação
DY = -(2*T+Y)./(2*Y);
DT = ones(size(DY));

% Normaliza os vetores
L = sqrt(DT.^2 + DY.^2);

% Evita divisão por zero para L
L(L==0) = 1;

% Plotar malha
quiver(T, Y, DT./L, DY./L, 0.5, 'b');

% Adiciona títulos e legendas
title("Campo de Direções para y' = -(2t + y) / (2y)");
xlabel('t');
ylabel('y');
axis tight;
