% Questão 24, equação y' = 3sen(t) + 1 + y

% Definindo o campo de direções
[T, Y] = meshgrid(0:0.5:10, -10:1:10);

% Definindo a equação
DY = 3*sin(T) + 1 + Y;
DT = ones(size(DY));

% Normalizar o comprimento das setas (melhor visualização)
L = sqrt(DT.^2 + DY.^2);

% Plotar malha
quiver(T, Y, DT./L, DY./L, 0.5, 'b');

% Adiciona títulos e legendas
title("Campo de Direções para y' = 3sen(t) + 1 + y");
xlabel('t');
ylabel('y');
axis tight;