import {select, scaleLinear} from "d3";
import {stepLayout} from "./layout.js";

const nodes = [{x: 20, y: 30}, {x: 70, y: 80}];
const links = [{source: 0, target: 1}];
stepLayout(nodes, links);
const x = scaleLinear().domain([0, 100]).range([0, 600]);
select("svg").selectAll("circle").data(nodes).join("circle")
  .attr("cx", d => x(d.x)).attr("cy", d => d.y).attr("r", 4);
