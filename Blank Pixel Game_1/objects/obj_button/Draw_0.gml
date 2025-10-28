// Draw the button sprite
draw_self();

// Draw the text "TEST" centered on the button
draw_set_color(c_white);
draw_set_halign(fa_center);
draw_set_valign(fa_middle);
draw_text(x + sprite_width/2, y + sprite_height/2, "TEST");
