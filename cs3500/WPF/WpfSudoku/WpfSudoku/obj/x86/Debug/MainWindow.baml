   M S B A M L   `   `   `  ����D  @WpfSudoku, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null%clr-namespace:WpfSudoku	WpfSudoku  5   	       WpfSudoku.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   'clrclr-namespace:WpfSudoku     5   	     � Title$  
MainWindow��5   	   $	��700��6   $	��800��6-   ��5      �� 6    �� ImageSource$ resources/tron.jpg��6$   .��5   
   ]� .+�5   
   �� $
��Left=�6   $	��150��6-   .+�5	      �� $	��Top=�6   $��40(�6/   ���#41f4f6 �� Padding$ 10q�6T   Sudoku6i   9� 5
       9� 
IsExpanded . $��	Main Menu��6+   .��5      �� $��5q�6    �� Padding$ 10q�6&   ���#e7fcfa���#41f4f6$��1q�6d   ._�5      �� .+�5      �� -   5        $��newGame��5   !   .��6H   
New Game6R   �� 5      -   5        $��loadGame��5   !   .��6J   	Load Game6U   �� 5      -   5        $��saveGame��5   !   .��6J   	Save Game6U   �� 5      -   5        $��quitGame��5   !   .��6F   Quit6L   5      5      5      9� 5       . $��New Game Settings��6+   ���#41f4f6.��5      �� $��5q�6   $ 10q�6&   ���#e7fcfa���#41f4f6$��1q�6c   ._�5      �� .+�5      �� ���#0c3935Board Size:6H   O Kmscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e0891&clr-namespace:System;assembly=mscorlibSystem 5   8   �� 6   4s&clr-namespace:System;assembly=mscorlib     68   -   5         ��Name$ 	BoardSize��5   #      BoardSizeTemplate#��[  6k    �� 
IsEditable .   �� SelectedItem 5      ��5   "   9��6-   .@�5      ��9��6)   ��5      16��6*   ��5      25��6*   ��5      36��6*   5       �� 5!      ���#0c3935Difficulty:6H   1&clr-namespace:System;assembly=mscorlibSystem 5"   9   �� 6   4s&clr-namespace:System;assembly=mscorlib     69   -   5        $ 
Difficulty��5"   #   #��[  6l    .  .@�5#      �� -   5        $��	ComboHard��5#   >    �� 
IsSelected . $
��Hard��6O   �� 5$      -   5        $��ComboMedium��5$   +   $��Medium��6>   �� 5%      -	   5        $��	ComboEasy��5%   +   $
��Easy��6<   5&      5'      5(      5)      9� 5*       . $��Timer��6+   .��5+      �� $��5q�6   $ 10q�6&   ���#e7fcfa���#41f4f6$��1q�6d   ._�5,      �� -
   5        $��timeText��5,   %   ���#0c3935.��6J   
00:00:006T   5-      5.      5/      �� 50   
   $	��Top=�6   $��20q�6+   �� 51   
   $��Bottom=�6   $��20q�6.      WpfSudoku.SudokuBoard  52   
   -   5        	  Name$	 Board��52      $��Stretch=�6+   $��Stretch=�6I   $��5q�6e   53      54      