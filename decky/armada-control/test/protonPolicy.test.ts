import assert from "node:assert/strict";
import test from "node:test";

import {
  CACHYOS_WINDOWS_COMPAT_TOOL,
  EXPERIMENTAL_WINDOWS_COMPAT_TOOL,
  PROTON_11_WINDOWS_COMPAT_TOOL,
  defaultWindowsCompatTool,
} from "../src/lib/protonPolicy.ts";

const tool = (id: string) => ({ id, label: id });

test("cachyos policy ignores other installed tools", () => {
  assert.equal(defaultWindowsCompatTool([
    tool(EXPERIMENTAL_WINDOWS_COMPAT_TOOL),
    tool(PROTON_11_WINDOWS_COMPAT_TOOL),
  ], "cachyos"), CACHYOS_WINDOWS_COMPAT_TOOL);
});

test("automatic policy prefers ARM Experimental then ARM Proton 11", () => {
  assert.equal(defaultWindowsCompatTool([
    tool(PROTON_11_WINDOWS_COMPAT_TOOL),
    tool(EXPERIMENTAL_WINDOWS_COMPAT_TOOL),
  ]), EXPERIMENTAL_WINDOWS_COMPAT_TOOL);
  assert.equal(defaultWindowsCompatTool([
    tool(PROTON_11_WINDOWS_COMPAT_TOOL),
  ]), PROTON_11_WINDOWS_COMPAT_TOOL);
});

test("automatic policy falls back to ARM CachyOS and ignores x86 tools", () => {
  assert.equal(defaultWindowsCompatTool([
    tool("proton_experimental"),
    tool("proton-stable"),
  ]), CACHYOS_WINDOWS_COMPAT_TOOL);
});
