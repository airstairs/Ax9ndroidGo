var camera, scene, renderer;
var geometry, material, mesh;

scene = new THREE.Scene();

geometry = new THREE.IcosahedronGeometry(200, 1);


material = new THREE.MeshNormalMaterial({ 
	wireframe: true, wireframeLinewidth: 4
});
mesh = new THREE.Mesh(geometry, material);

scene.add(mesh);

renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
camera.position.z = 500;

renderer.render(scene, camera);
