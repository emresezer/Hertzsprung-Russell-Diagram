<h1 align="center">⭐ Hertzsprung–Russell Diagram</h1>
<p align="center">
  <em>Visualizing stellar evolution and properties with Python</em>
</p>

<hr>

<h2>🎯 Purpose & Scope</h2>
<p>
  This repository offers a Python‐based visualization of the <strong>Hertzsprung–Russell (H-R) Diagram</strong>, 
  a fundamental tool in astrophysics that plots stars by luminosity (or magnitude) vs. temperature (or spectral class). 
  The aim is to provide both educational insight and analytical visualization of stellar populations.
</p>
<ul>
  <li>Plot the positions of stars in the H-R plane.</li>
  <li>Use real or synthetic stellar data (temperature, luminosity, magnitude).</li>
  <li>Generate bilingual (Turkish / English) output images.</li>
  <li>Enable comparison of different stellar populations or evolutionary tracks.</li>
</ul>

<hr>

<h2>🧩 Project Structure</h2>

<pre>
📁 Hertzsprung-Russell-Diagram/
│
├── Python Doc.py          → Main script: data processing & plotting routines
├── HR image_en.png         → H-R diagram (English labels)
├── HR image_tr.png         → H-R diagram (Turkish labels)
└── README.md               → This file (with HTML content)
</pre>

<hr>

<h2>⚙️ Installation & Usage</h2>
<ol>
  <li>Ensure you have <strong>Python 3.x</strong> installed.</li>
  <li>Install required libraries (e.g. <code>numpy</code>, <code>matplotlib</code>):  
    <pre><code>pip install numpy matplotlib</code></pre>
  </li>
  <li>Run the plotting script:
    <pre><code>python "Python Doc.py"</code></pre>
  </li>
  <li>Resulting H-R diagram images are saved in the repo (English and Turkish versions).</li>
  <li>Optionally modify input stellar datasets or add your own data to visualize different groups.</li>
</ol>

<hr>

<h2>🔭 Scientific Background</h2>

<h3>• Hertzsprung–Russell Diagram Explained</h3>
<p>
  The H-R diagram is a scatter plot where stars are placed according to:
  <ul>
    <li><strong>Surface temperature (or spectral class)</strong> on the horizontal axis, usually decreasing leftwards</li>
    <li><strong>Luminosity (or absolute magnitude)</strong> on the vertical axis</li>
  </ul>
  This diagram reveals stellar populations: the main sequence, giants, supergiants, white dwarfs, etc.
</p>

<h3>• Typical Relations</h3>
<p>
  - More massive, hotter stars tend to lie toward the upper left (high luminosity, high temperature).  
  - Cooler, less luminous stars lie toward the lower right.  
  - Evolutionary tracks move stars across this diagram as they age.
</p>
