% Exercício 23, equação y' = e^-t + y

% Definindo o campo de direções
[T, Y] = meshgrid(0:0.5:10, -5:0.5:5);

% Definindo a equação
DY = exp(-T) + Y;
DT = ones(size(DY));

% Normalizar o comprimento das setas (melhor visualização)
L = sqrt(DT.^2 + DY.^2);

% Plotar malha
quiver(T, Y, DT./L, DY./L, 0.5, 'b');

% Adiciona títulos e legendas
title("Campo de Direções para y' = e^{-t} + y");
xlabel('t');
ylabel('y');
axis tight;