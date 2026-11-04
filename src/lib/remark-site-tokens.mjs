import { SITE } from '../config/site.ts';

const TOKENS = { '{{PRICE_FRONT_DESK}}': SITE.PRICE_FRONT_DESK };

/** Replaces {{TOKEN}} placeholders in Markdown text, links and HTML nodes with values from SITE. */
export default function remarkSiteTokens() {
  const replace = (s) => Object.entries(TOKENS).reduce((acc, [k, v]) => acc.replaceAll(k, v), s);
  const walk = (node) => {
    if (typeof node.value === 'string') node.value = replace(node.value);
    if (typeof node.url === 'string') node.url = replace(node.url);
    node.children?.forEach(walk);
  };
  return (tree) => walk(tree);
}
