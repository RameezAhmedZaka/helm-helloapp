{{- define "hellohelm.name" -}}
hellohelm
{{- end }}

{{- define "hellohelm.fullname" -}}
{{- printf "%s-%s" .Release.Name "hellohelm" | trunc 63 | trimSuffix "-" }}
{{- end }}
