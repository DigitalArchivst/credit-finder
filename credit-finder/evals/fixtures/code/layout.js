// Spring attraction is computed here. There are no imports in this file.
export function stepLayout(nodes, links, spring = 0.02) {
  for (const {source, target} of links) {
    const a = nodes[source];
    const b = nodes[target];
    const dx = (b.x - a.x) * spring;
    const dy = (b.y - a.y) * spring;
    a.x += dx; a.y += dy;
    b.x -= dx; b.y -= dy;
  }
}
