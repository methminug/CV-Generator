def add_cv_configs():
    configurations = r'''
    %!TEX TS-program = xelatex
    %!TEX encoding = UTF-8 Unicode
    % Awesome CV LaTeX Template for CV/Resume
    %
    % This template has been downloaded from:
    % https://github.com/posquit0/Awesome-CV
    %
    % Author:
    % Claud D. Park <posquit0.bj@gmail.com>
    % http://www.posquit0.com
    %
    % Template license:
    % CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
    %


    %-------------------------------------------------------------------------------
    % CONFIGURATIONS
    %-------------------------------------------------------------------------------
    % A4 paper size by default, use 'letterpaper' for US letter
    \documentclass[11pt, a4paper]{awesome-cv}

    % Configure page margins with geometry
    \geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

    % Color for highlights
    % Awesome Colors: awesome-emerald, awesome-skyblue, awesome-red, awesome-pink, awesome-orange
    %                 awesome-nephritis, awesome-concrete, awesome-darknight
    \colorlet{awesome}{awesome-red}
    % Uncomment if you would like to specify your own color
    % \definecolor{awesome}{HTML}{CA63A8}

    % Colors for text
    % Uncomment if you would like to specify your own color
    % \definecolor{darktext}{HTML}{414141}
    % \definecolor{text}{HTML}{333333}
    % \definecolor{graytext}{HTML}{5D5D5D}
    % \definecolor{lighttext}{HTML}{999999}

    % Set false if you don't want to highlight section with awesome color
    \setbool{acvSectionColorHighlight}{true}

    '''

    with open("cv.tex", 'w') as file:
        file.write(configurations)
