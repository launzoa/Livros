% Problema y´ = 1 + 2y

% Definir o intervalo e a densidade da malha para t e y
[T, Y] = meshgrid(0:0.4:8, -2:0.4:5);

% Definir a equação diferencial dy/dt
DY = 1 + 2*Y;
DT = ones(size(DY)); % Componente DT é sempre 1

% Normalizar o comprimento das setas (melhor visualização)
L = sqrt(DT.^2 + DY.^2);
DY_norm = DY./L;
DT_norm = DT./L;

% Plotar o campo de direções
quiver(T,Y, DT_norm, DY_norm, 0.5, 'b');

% Plotar a solução de equilíbrio y = -0.5
hold on;
plot([0 8], [-0.5 -0.5], 'r', 'LineWidth', 2);
hold off;

title("Campo de direções para y´ = 1 + 2y");
xlabel('t');
ylabel('y');