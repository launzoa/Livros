% Equação -> y(t) = b/a + C*e^{-at}
% onde, C = {y0 - b/a}

% Vamos usar a = 1 e b = 3, por exemplo
% Equação -> y(t) = 3 - y
% Solução de equilíbrio -> ye = 3
% Solução para condição inicia -> y(t) = 3 + {y0 - 3)e^t

% Parâmetros da equação
a = 1;
b = 3;

% Solução de equilíbrio
y_eq = b/a;

% Intervalo do gráfico
t = 0:0.1:5;

% Condições iniciais 
y0_values = [-1, 0, 1, 5, 7];

% Criando a figura e ativa 'hold on' para plotar todas as curvas no mesmo
% gráfico
figure;
hold on;
grid on;

% Loop para plotar a solução para cada condição inicial
for i = 1:length(y0_values)
    y0 = y0_values(i);

    C = y0 - y_eq;

    y = y_eq + C * exp(-a*t);

    plot(t, y, 'LineWidth', 1.5);
end

% Linha tracejada da solução de equilíbrio 
plot(t, y_eq * ones(size(t)), 'r--', 'LineWidth', 2);

% Títulos e Legendas
title(['Soluções de y'' = -', num2str(a), 'y + ', num2str(b)]);
xlabel('Tempo (t)');
ylabel('y(t)');
legend_text = arrayfun(@(y) ['y(0) = ' num2str(y)], y0_values, 'UniformOutput', false);
legend_text{end+1} = ['Equilíbrio y = ' num2str(y_eq)];
legend(legend_text, 'Location', 'best');

hold off;



