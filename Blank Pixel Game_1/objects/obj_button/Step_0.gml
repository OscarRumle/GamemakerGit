// Check if mouse is hovering over button
is_hovered = position_meeting(mouse_x, mouse_y, obj_button);

// Change sprite frame based on hover state
if (is_hovered) {
    image_index = 1; // Hover state
} else {
    image_index = 0; // Normal state
}
