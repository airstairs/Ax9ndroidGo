// 1. Create the Scene (the 3D world)
const scene = new THREE.Scene();

// 2. Create the Camera (the viewpoint)
// Parameters: Field of View (75°), Aspect Ratio, Near clipping plane, Far clipping plane
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5; // Move the camera back so we can see the cube

// 3. Create the Renderer (the engine that draws the 3D scene onto your 2D screen)
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement); // Inject the canvas into the HTML

// 4. Create the Cube (Geometry + Material = Mesh)
const geometry = new THREE.BoxGeometry(1, 1, 1); // Width, height, depth
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true }); // Green wireframe
const cube = new THREE.Mesh(geometry, material);
scene.add(cube); // Add the cube to our world

// 5. Animation Loop (runs roughly 60 times per second)
function animate() {
    requestAnimationFrame(animate);

    // Rotate the cube a tiny bit every frame
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    // Render the scene from the perspective of the camera
    renderer.render(scene, camera);
}

// Start the animation
animate();

// 6. Handle Window Resizing (keeps things looking sharp if you resize your browser)
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
