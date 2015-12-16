<?php

chdir(__DIR__. '/../');

echo json_encode([
    'time'   => time(),
    'supply' => include 'data/supply.php',
    'state'  => json_decode(file_get_contents('data/state.json'), true),
    'events' => json_decode(file_get_contents('data/events.json'), true),
]);
