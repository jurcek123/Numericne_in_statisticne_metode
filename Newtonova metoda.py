function [x,X,k] = newton(F,JF,x0,tol,maxk,info)
% Opis:
%  newton izvede Newtonovo metodo za resevanje sistema nelinearnih enacb.
%
% Definicija:
%  x = newton(F,JF,x0,tol,maxk,info)
%
% Vhodni podatki:
%  F        preslikava, ki doloca sistem v obliki F(x) = 0,
%  JF       preslikava, ki doloca Jacobijevo matriko preslikave F,
%  x0       vektor, ki predstavlja zacetni priblizek za Newtonovo metodo,
%  tol      toleranca absolutnega ujemanja dveh zaporednih priblizkov
%           (privzeto 1e-10),
%  maxk     maksimalno stevilo korakov iteracije (privzeto 50),
%  info     parameter, ki doloca, ali se med izvedbo metode izpisujejo
%           informacije o priblizkih in neskoncni normi razlike med
%           zaporednima priblizkoma (privzeto false).
%
% Izhodni podatki:
%  x        priblizek za resitev sistema F(x) = 0,
%  X        tabela, v kateri stolpci predstavljajo priblizke za resitev
%           sistema F(x) = 0 od prvega proti zadnjemu izracunanemu,
%  k        stevilo opravljenih korakov iteracije.

if nargin < 4, tol = 1e-10; end
if nargin < 5, maxk = 50; end
if nargin < 6, info = false; end

X = [x0 zeros(length(x0),maxk)];

dx = 2*tol*x0 + 1;
k = 0;
while norm(dx) > tol && k < maxk
   x0 = X(:,k+1);
   k = k+1;
   dx = -JF(x0)\F(x0);
   X(:,k+1) = x0 + dx;
   if info
       % izpisemo trenutni priblizek
       fprintf('%3 d: % s %0 .1e \n', k, sprintf('%15 .15f ',X(:,k+1)), norm(dx,Inf));
   end
end

X = X(:,1:k+1);
x = X(:,k+1);

end