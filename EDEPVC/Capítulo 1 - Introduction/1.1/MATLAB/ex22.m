% Questão 22, equação y' = -2 + t - y

% Definir o intervalo e a densidade da malha para t e y
[T, Y] = meshgrid(0:0.5:10, -5:0.5:5);

% Definindo a equação
DY =  -2 + T - Y;
DT = ones(size(DY));

% Normalizar o comprimento das setas (melhor visualização)
L = sqrt(DT.^2 + DY.^2);

quiver(T, Y, DT./L, DY./L, 0.5, 'b');


title("Campo de direções para y' = -2 + t - y");
xlabel('t');
ylabel('y');
axis tight;
legend('Campo de Direções', 'Assíntota y = t - 2');
