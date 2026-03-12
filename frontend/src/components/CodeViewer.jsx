import { PrismLight as SyntaxHighlighter } from 'react-syntax-highlighter';
import jsx from 'react-syntax-highlighter/dist/esm/languages/prism/jsx';
import python from 'react-syntax-highlighter/dist/esm/languages/prism/python';
import c from 'react-syntax-highlighter/dist/esm/languages/prism/c';
import cpp from 'react-syntax-highlighter/dist/esm/languages/prism/cpp';
import java from 'react-syntax-highlighter/dist/esm/languages/prism/java';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';

SyntaxHighlighter.registerLanguage('jsx', jsx);
SyntaxHighlighter.registerLanguage('python', python);
SyntaxHighlighter.registerLanguage('c', c);
SyntaxHighlighter.registerLanguage('cpp', cpp);
SyntaxHighlighter.registerLanguage('java', java);

export default function CodeViewer({ code, language = 'python', copiedLines = [], filename = "source.js" }) {
  // Try mapping the language or standardizing it for Prism.
  const mapLanguage = (lang) => {
    const l = lang?.toLowerCase();
    if (l === 'c' || l === 'cpp' || l === 'c++') return 'cpp';
    if (l === 'java') return 'java';
    if (l === 'python' || l === 'py') return 'python';
    return 'javascript';
  };

  return (
    <div className="rounded-xl overflow-hidden border border-white/10 shadow-2xl glass-card flex flex-col h-full bg-[#1e1e1e]">
      <div className="flex items-center justify-between px-4 py-3 border-b border-white/10 bg-[#1e1e1e]/80 shrink-0">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5 mr-2">
            <div className="w-3 h-3 rounded-full bg-rose-500/80"></div>
            <div className="w-3 h-3 rounded-full bg-amber-500/80"></div>
            <div className="w-3 h-3 rounded-full bg-emerald-500/80"></div>
          </div>
          <span className="text-xs font-mono text-slate-400">{filename}</span>
        </div>
      </div>
      <div className="flex-1 overflow-auto custom-scrollbar relative">
        <SyntaxHighlighter
          language={mapLanguage(language)}
          style={vscDarkPlus}
          showLineNumbers={true}
          wrapLines={true}
          customStyle={{
            margin: 0,
            padding: '1.5rem',
            background: 'transparent',
            fontSize: '13px',
            lineHeight: '1.6',
          }}
          lineNumberStyle={{
            minWidth: '2.5em',
            paddingRight: '1em',
            color: '#6e7681',
            textAlign: 'right'
          }}
          lineProps={(lineNumber) => {
            const style = { display: 'block', padding: '0 4px', borderRadius: '4px' };
            if (copiedLines && copiedLines.includes(lineNumber)) {
              style.backgroundColor = 'rgba(239, 68, 68, 0.15)'; // red-500/15
              style.borderLeft = '4px solid #ef4444'; 
              style.paddingLeft = '0px'; 
            }
            return { style };
          }}
        >
          {code || "No code available."}
        </SyntaxHighlighter>
      </div>
    </div>
  );
}
