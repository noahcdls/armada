export interface CompatTool {
  id: string;
  label: string;
}

export const EXPERIMENTAL_WINDOWS_COMPAT_TOOL = "proton-experimental-arm64";
export const PROTON_11_WINDOWS_COMPAT_TOOL = "proton-stable-arm64";
// Keep in sync with PROTON_TOOL_NAME (build) and PROTON_11_STABLE (armada-fixups).
export const CACHYOS_WINDOWS_COMPAT_TOOL = "proton-cachyos-11.0-arm64";

export function defaultWindowsCompatTool(tools: CompatTool[], policy = "automatic"): string {
  if (policy === "cachyos") return CACHYOS_WINDOWS_COMPAT_TOOL;
  if (tools.some((tool) => tool.id === EXPERIMENTAL_WINDOWS_COMPAT_TOOL)) {
    return EXPERIMENTAL_WINDOWS_COMPAT_TOOL;
  }
  if (tools.some((tool) => tool.id === PROTON_11_WINDOWS_COMPAT_TOOL)) {
    return PROTON_11_WINDOWS_COMPAT_TOOL;
  }
  return CACHYOS_WINDOWS_COMPAT_TOOL;
}
